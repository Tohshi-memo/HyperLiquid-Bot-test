# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T00:52:30.530756+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `13`; crypto_alt avg `0.1496` n `235`; crypto_major avg `0.0239` n `8`; equity avg `-0.1021` n `150`; fx avg `0.0017` n `6`; index avg `-0.0245` n `26`; metal avg `-0.0137` n `20`; unknown avg `0.0202` n `1076`
- 1h: commodity avg `0.0504` n `13`; crypto_alt avg `0.0424` n `235`; crypto_major avg `-0.0581` n `8`; equity avg `0.1132` n `150`; fx avg `0.0055` n `6`; index avg `0.0326` n `26`; metal avg `-0.0438` n `20`; unknown avg `0.12` n `1068`
- 4h: commodity avg `0.0797` n `13`; crypto_alt avg `0.0305` n `235`; crypto_major avg `-0.0924` n `8`; equity avg `0.1285` n `150`; fx avg `0.0231` n `6`; index avg `0.0327` n `26`; metal avg `-0.0216` n `20`; unknown avg `-0.1106` n `1046`
- 24h: commodity avg `0.4237` n `13`; crypto_alt avg `-0.8853` n `235`; crypto_major avg `-0.9549` n `8`; equity avg `0.4328` n `149`; fx avg `0.104` n `6`; index avg `0.0268` n `26`; metal avg `-0.0534` n `20`; unknown avg `870.7624` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1633`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
