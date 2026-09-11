# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T04:22:28.575034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1006` n `12`; crypto_alt avg `0.3456` n `233`; crypto_major avg `0.1577` n `8`; equity avg `0.0853` n `136`; fx avg `-0.0115` n `6`; index avg `0.0214` n `26`; metal avg `0.0835` n `20`; unknown avg `1.1866` n `796`
- 1h: commodity avg `-0.135` n `12`; crypto_alt avg `0.8819` n `233`; crypto_major avg `0.4469` n `8`; equity avg `0.1586` n `136`; fx avg `-0.0294` n `6`; index avg `0.0422` n `26`; metal avg `0.1256` n `20`; unknown avg `1.9006` n `792`
- 4h: commodity avg `-0.1136` n `12`; crypto_alt avg `0.5291` n `233`; crypto_major avg `0.349` n `8`; equity avg `-0.1175` n `136`; fx avg `-0.0735` n `6`; index avg `0.0345` n `26`; metal avg `0.029` n `20`; unknown avg `-0.588` n `780`
- 24h: commodity avg `1.0689` n `12`; crypto_alt avg `-1.6032` n `233`; crypto_major avg `-2.2195` n `8`; equity avg `-2.0686` n `136`; fx avg `0.0563` n `6`; index avg `-0.3323` n `26`; metal avg `-1.2649` n `20`; unknown avg `-1.026` n `675`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
