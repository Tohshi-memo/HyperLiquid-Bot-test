# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T10:07:13.449141+00:00`
- Correlation status: `ready`
- Asset price records: `540`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.06` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1052` n `12`; crypto_alt avg `0.157` n `228`; crypto_major avg `0.0826` n `8`; equity avg `-0.182` n `65`; fx avg `-0.0162` n `4`; index avg `-0.0273` n `23`; metal avg `-0.0415` n `18`; unknown avg `0.0073` n `358`
- 1h: commodity avg `0.0948` n `12`; crypto_alt avg `-0.0152` n `228`; crypto_major avg `-0.0579` n `8`; equity avg `0.3056` n `65`; fx avg `-0.0234` n `4`; index avg `-0.0998` n `23`; metal avg `0.1756` n `18`; unknown avg `0.1492` n `358`
- 4h: commodity avg `-0.5491` n `12`; crypto_alt avg `0.6457` n `228`; crypto_major avg `0.2195` n `8`; equity avg `0.3342` n `65`; fx avg `0.0159` n `4`; index avg `-0.0599` n `23`; metal avg `1.073` n `18`; unknown avg `0.4699` n `358`
- 24h: commodity avg `-0.3947` n `7`; crypto_alt avg `-0.0875` n `223`; crypto_major avg `-2.0301` n `7`; equity avg `0.3996` n `47`; fx avg `0.1053` n `4`; index avg `0.431` n `6`; metal avg `1.1929` n `7`; unknown avg `0.7333` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.131`, n `536`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1236`, n `536`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0977`, n `536`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0914`, n `532`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0835`, n `532`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0808`, n `532`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0792`, n `532`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0768`, n `532`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0699`, n `532`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0657`, n `536`, weak_sample_signal
