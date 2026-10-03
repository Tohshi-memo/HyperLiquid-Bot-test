# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T14:07:32.964772+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `13`; crypto_alt avg `-0.0431` n `235`; crypto_major avg `-0.0403` n `8`; equity avg `-0.0044` n `143`; fx avg `-0.0005` n `6`; index avg `-0.0003` n `26`; metal avg `0.001` n `20`; unknown avg `0.0021` n `978`
- 1h: commodity avg `0.0899` n `13`; crypto_alt avg `0.1289` n `235`; crypto_major avg `-0.0628` n `8`; equity avg `-0.0102` n `143`; fx avg `-0.0025` n `6`; index avg `0.0072` n `26`; metal avg `-0.0056` n `20`; unknown avg `0.1854` n `964`
- 4h: commodity avg `0.037` n `13`; crypto_alt avg `0.2871` n `235`; crypto_major avg `0.1834` n `8`; equity avg `-0.0029` n `143`; fx avg `-0.0116` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0047` n `20`; unknown avg `0.076` n `954`
- 24h: commodity avg `0.7616` n `13`; crypto_alt avg `-2.1467` n `235`; crypto_major avg `-1.9543` n `8`; equity avg `-0.6653` n `143`; fx avg `-0.0424` n `6`; index avg `-0.0969` n `26`; metal avg `-0.3602` n `20`; unknown avg `0.6387` n `876`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.197`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1866`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1599`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
