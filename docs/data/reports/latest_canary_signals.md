# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T11:37:28.418276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.023` n `12`; crypto_alt avg `0.214` n `230`; crypto_major avg `0.274` n `8`; equity avg `0.0286` n `92`; fx avg `-0.006` n `6`; index avg `-0.0001` n `25`; metal avg `0.0025` n `20`; unknown avg `0.0404` n `765`
- 1h: commodity avg `0.0199` n `12`; crypto_alt avg `0.0632` n `230`; crypto_major avg `0.3229` n `8`; equity avg `0.0891` n `92`; fx avg `-0.0055` n `6`; index avg `-0.0037` n `25`; metal avg `0.0002` n `20`; unknown avg `-0.0917` n `763`
- 4h: commodity avg `0.0542` n `12`; crypto_alt avg `0.1104` n `230`; crypto_major avg `0.4258` n `8`; equity avg `0.0883` n `92`; fx avg `-0.0009` n `6`; index avg `0.0038` n `25`; metal avg `-0.0113` n `20`; unknown avg `-0.0753` n `763`
- 24h: commodity avg `0.5309` n `12`; crypto_alt avg `-0.8909` n `230`; crypto_major avg `-0.5198` n `8`; equity avg `-0.1251` n `92`; fx avg `0.0061` n `6`; index avg `-0.1243` n `25`; metal avg `-0.1057` n `20`; unknown avg `0.1266` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1767`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1609`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.131`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1243`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.121`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1177`, n `669`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1105`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1044`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1028`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1006`, n `669`, weak_sample_signal
