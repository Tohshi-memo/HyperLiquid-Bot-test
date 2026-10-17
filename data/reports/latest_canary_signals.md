# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T09:07:25.012022+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `13`; crypto_alt avg `-0.0401` n `236`; crypto_major avg `-0.0089` n `8`; equity avg `0.0093` n `151`; fx avg `-0.0055` n `6`; index avg `-0.0076` n `26`; metal avg `-0.0004` n `20`; unknown avg `-0.0849` n `1191`
- 1h: commodity avg `0.0467` n `13`; crypto_alt avg `-0.0572` n `236`; crypto_major avg `-0.0729` n `8`; equity avg `0.0329` n `151`; fx avg `-0.018` n `6`; index avg `-0.016` n `26`; metal avg `0.0114` n `20`; unknown avg `-0.0581` n `1191`
- 4h: commodity avg `-0.1916` n `13`; crypto_alt avg `-0.5521` n `236`; crypto_major avg `0.0236` n `8`; equity avg `0.0179` n `151`; fx avg `-0.0169` n `6`; index avg `0.0182` n `26`; metal avg `0.0001` n `20`; unknown avg `0.0095` n `1157`
- 24h: commodity avg `0.4442` n `13`; crypto_alt avg `-2.1552` n `236`; crypto_major avg `-1.4365` n `8`; equity avg `-3.7452` n `151`; fx avg `-0.0024` n `6`; index avg `-0.5853` n `26`; metal avg `-0.2807` n `20`; unknown avg `8.5724` n `954`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1804`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1462`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1238`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1214`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0757`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
