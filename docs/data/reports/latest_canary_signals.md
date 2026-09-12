# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T00:07:28.346913+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.11` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0103` n `12`; crypto_alt avg `0.1229` n `233`; crypto_major avg `-0.1193` n `8`; equity avg `0.0606` n `136`; fx avg `-0.006` n `6`; index avg `0.0162` n `26`; metal avg `-0.0036` n `20`; unknown avg `0.0579` n `834`
- 1h: commodity avg `-0.0381` n `12`; crypto_alt avg `0.4926` n `233`; crypto_major avg `0.1585` n `8`; equity avg `0.0948` n `136`; fx avg `-0.0106` n `6`; index avg `0.0127` n `26`; metal avg `-0.0136` n `20`; unknown avg `-0.0901` n `832`
- 4h: commodity avg `-0.1136` n `12`; crypto_alt avg `-0.5622` n `233`; crypto_major avg `-0.7661` n `8`; equity avg `0.0466` n `136`; fx avg `-0.0387` n `6`; index avg `0.0185` n `26`; metal avg `-0.0376` n `20`; unknown avg `6.719` n `800`
- 24h: commodity avg `-0.6296` n `12`; crypto_alt avg `0.8854` n `233`; crypto_major avg `1.3664` n `8`; equity avg `0.9506` n `136`; fx avg `-0.1831` n `6`; index avg `0.3425` n `26`; metal avg `0.2338` n `20`; unknown avg `2.2503` n `702`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
