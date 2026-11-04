# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T23:52:27.398512+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0212` n `13`; crypto_alt avg `-0.0473` n `239`; crypto_major avg `-0.0189` n `8`; equity avg `-0.0361` n `158`; fx avg `-0.0063` n `6`; index avg `-0.0289` n `27`; metal avg `0.0553` n `20`; unknown avg `3.6936` n `1264`
- 1h: commodity avg `0.0158` n `13`; crypto_alt avg `-0.6284` n `239`; crypto_major avg `-0.3215` n `8`; equity avg `-0.3531` n `158`; fx avg `0.0085` n `6`; index avg `-0.0898` n `27`; metal avg `0.0565` n `20`; unknown avg `0.0255` n `1202`
- 4h: commodity avg `-0.0388` n `13`; crypto_alt avg `0.9344` n `239`; crypto_major avg `0.7785` n `8`; equity avg `0.2087` n `158`; fx avg `0.0112` n `6`; index avg `0.0074` n `27`; metal avg `0.085` n `20`; unknown avg `351.1187` n `1138`
- 24h: commodity avg `-1.8046` n `13`; crypto_alt avg `1.6336` n `239`; crypto_major avg `2.2342` n `8`; equity avg `-1.5495` n `158`; fx avg `0.0492` n `6`; index avg `0.0448` n `27`; metal avg `1.258` n `20`; unknown avg `29.5979` n `1036`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2657`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
