# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T09:52:33.581601+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.04` n `13`; crypto_alt avg `0.214` n `238`; crypto_major avg `0.146` n `8`; equity avg `0.1187` n `155`; fx avg `0.009` n `6`; index avg `0.0458` n `27`; metal avg `-0.0148` n `20`; unknown avg `0.9526` n `1236`
- 1h: commodity avg `0.019` n `13`; crypto_alt avg `0.5442` n `238`; crypto_major avg `0.3072` n `8`; equity avg `0.3929` n `155`; fx avg `0.0047` n `6`; index avg `0.1644` n `27`; metal avg `-0.0198` n `20`; unknown avg `0.5888` n `1224`
- 4h: commodity avg `0.0454` n `13`; crypto_alt avg `-0.5289` n `238`; crypto_major avg `-0.3286` n `8`; equity avg `-0.3067` n `155`; fx avg `0.0152` n `6`; index avg `0.0345` n `27`; metal avg `-0.1932` n `20`; unknown avg `-0.4057` n `1190`
- 24h: commodity avg `-0.0502` n `13`; crypto_alt avg `-2.6706` n `238`; crypto_major avg `-2.0294` n `8`; equity avg `-1.3616` n `155`; fx avg `0.0339` n `6`; index avg `0.0427` n `27`; metal avg `-0.4684` n `20`; unknown avg `25.0109` n `1000`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
