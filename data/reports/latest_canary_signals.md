# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T07:07:24.927011+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0346` n `13`; crypto_alt avg `-0.0712` n `236`; crypto_major avg `0.0149` n `8`; equity avg `0.0189` n `151`; fx avg `0.0011` n `6`; index avg `-0.0051` n `26`; metal avg `0.0008` n `20`; unknown avg `0.0434` n `1191`
- 1h: commodity avg `-0.2003` n `13`; crypto_alt avg `-0.113` n `236`; crypto_major avg `0.1062` n `8`; equity avg `0.0372` n `151`; fx avg `0.0011` n `6`; index avg `-0.0124` n `26`; metal avg `0.0134` n `20`; unknown avg `0.0456` n `1189`
- 4h: commodity avg `-0.2301` n `13`; crypto_alt avg `0.2078` n `236`; crypto_major avg `0.3562` n `8`; equity avg `0.1344` n `151`; fx avg `-0.0015` n `6`; index avg `0.0231` n `26`; metal avg `0.0076` n `20`; unknown avg `0.6124` n `1167`
- 24h: commodity avg `0.2901` n `13`; crypto_alt avg `-1.9508` n `236`; crypto_major avg `-1.2138` n `8`; equity avg `-3.8039` n `151`; fx avg `0.0607` n `6`; index avg `-0.5931` n `26`; metal avg `-0.2226` n `20`; unknown avg `40.6574` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1801`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1329`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1245`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1137`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0747`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
