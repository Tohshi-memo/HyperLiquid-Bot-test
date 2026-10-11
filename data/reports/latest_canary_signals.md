# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T08:01:12.875157+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `13`; crypto_alt avg `-0.0399` n `235`; crypto_major avg `-0.0044` n `8`; equity avg `-0.012` n `150`; fx avg `-0.0006` n `6`; index avg `-0.0005` n `26`; metal avg `-0.0023` n `20`; unknown avg `0.0327` n `1099`
- 1h: commodity avg `0.0023` n `13`; crypto_alt avg `-0.2314` n `235`; crypto_major avg `-0.1862` n `8`; equity avg `-0.0343` n `150`; fx avg `0.0` n `6`; index avg `-0.0017` n `26`; metal avg `0.0043` n `20`; unknown avg `0.9388` n `1099`
- 4h: commodity avg `0.0238` n `13`; crypto_alt avg `1.0643` n `235`; crypto_major avg `0.1607` n `8`; equity avg `0.0469` n `150`; fx avg `0.0017` n `6`; index avg `0.013` n `26`; metal avg `0.0157` n `20`; unknown avg `0.4689` n `1083`
- 24h: commodity avg `0.1654` n `13`; crypto_alt avg `0.9587` n `235`; crypto_major avg `-0.3191` n `8`; equity avg `0.0389` n `150`; fx avg `-0.0265` n `6`; index avg `0.0018` n `26`; metal avg `0.0035` n `20`; unknown avg `0.638` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
