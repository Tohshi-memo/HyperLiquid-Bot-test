# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T13:22:28.591314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0245` n `12`; crypto_alt avg `-0.2299` n `234`; crypto_major avg `-0.1346` n `8`; equity avg `-0.0591` n `141`; fx avg `-0.0037` n `6`; index avg `-0.0064` n `26`; metal avg `-0.0346` n `20`; unknown avg `136.9718` n `962`
- 1h: commodity avg `-0.1259` n `12`; crypto_alt avg `-0.3832` n `234`; crypto_major avg `-0.0827` n `8`; equity avg `-0.1435` n `141`; fx avg `0.0064` n `6`; index avg `-0.0077` n `26`; metal avg `-0.2072` n `20`; unknown avg `22.4833` n `960`
- 4h: commodity avg `-0.1986` n `12`; crypto_alt avg `0.8059` n `234`; crypto_major avg `0.8232` n `8`; equity avg `0.3884` n `141`; fx avg `-0.023` n `6`; index avg `0.0678` n `26`; metal avg `-0.0226` n `20`; unknown avg `46.6344` n `954`
- 24h: commodity avg `-0.3164` n `12`; crypto_alt avg `-2.359` n `234`; crypto_major avg `-1.802` n `8`; equity avg `-2.5173` n `141`; fx avg `0.0032` n `6`; index avg `-0.1941` n `26`; metal avg `-0.9848` n `20`; unknown avg `4.0002` n `814`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
