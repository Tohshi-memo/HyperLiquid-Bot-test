# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T07:52:28.520507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0855` n `13`; crypto_alt avg `0.007` n `235`; crypto_major avg `-0.0101` n `8`; equity avg `-0.0495` n `150`; fx avg `-0.0106` n `6`; index avg `-0.0241` n `26`; metal avg `-0.0026` n `20`; unknown avg `4.1985` n `1076`
- 1h: commodity avg `0.0506` n `13`; crypto_alt avg `0.1379` n `235`; crypto_major avg `-0.0088` n `8`; equity avg `-0.1269` n `150`; fx avg `-0.0681` n `6`; index avg `-0.0263` n `26`; metal avg `0.0228` n `20`; unknown avg `4.522` n `1074`
- 4h: commodity avg `0.1475` n `13`; crypto_alt avg `0.1239` n `235`; crypto_major avg `0.2789` n `8`; equity avg `-0.2752` n `150`; fx avg `-0.0918` n `6`; index avg `-0.086` n `26`; metal avg `-0.1639` n `20`; unknown avg `1.7974` n `1046`
- 24h: commodity avg `0.8927` n `13`; crypto_alt avg `-3.0236` n `235`; crypto_major avg `-1.8587` n `8`; equity avg `-0.3449` n `149`; fx avg `-0.0345` n `6`; index avg `-0.1314` n `26`; metal avg `-0.1891` n `20`; unknown avg `814.3221` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1737`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
