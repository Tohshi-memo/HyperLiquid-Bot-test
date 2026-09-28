# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T08:37:32.191849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0254` n `12`; crypto_alt avg `-0.2032` n `234`; crypto_major avg `-0.0856` n `8`; equity avg `-0.0603` n `141`; fx avg `0.0026` n `6`; index avg `-0.0105` n `26`; metal avg `-0.0598` n `20`; unknown avg `0.015` n `962`
- 1h: commodity avg `0.1466` n `12`; crypto_alt avg `-0.0696` n `234`; crypto_major avg `-0.0611` n `8`; equity avg `-0.3544` n `141`; fx avg `-0.0869` n `6`; index avg `-0.0186` n `26`; metal avg `-0.0217` n `20`; unknown avg `0.9543` n `944`
- 4h: commodity avg `0.1774` n `12`; crypto_alt avg `-1.7665` n `234`; crypto_major avg `-0.9744` n `8`; equity avg `-1.2286` n `141`; fx avg `-0.0757` n `6`; index avg `-0.1067` n `26`; metal avg `-0.3141` n `20`; unknown avg `29.7848` n `920`
- 24h: commodity avg `-0.1585` n `12`; crypto_alt avg `-4.2078` n `234`; crypto_major avg `-3.2927` n `8`; equity avg `-2.7202` n `141`; fx avg `-0.0189` n `6`; index avg `-0.2682` n `26`; metal avg `-1.0008` n `20`; unknown avg `6.2831` n `815`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
