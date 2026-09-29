# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T07:52:37.723146+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0207` n `12`; crypto_alt avg `0.057` n `234`; crypto_major avg `-0.0572` n `8`; equity avg `-0.0391` n `141`; fx avg `0.0135` n `6`; index avg `-0.0097` n `26`; metal avg `-0.0165` n `20`; unknown avg `3.7399` n `963`
- 1h: commodity avg `-0.1689` n `12`; crypto_alt avg `0.7377` n `234`; crypto_major avg `0.3027` n `8`; equity avg `0.2193` n `141`; fx avg `-0.0345` n `6`; index avg `0.0164` n `26`; metal avg `-0.0262` n `20`; unknown avg `3.8038` n `961`
- 4h: commodity avg `-0.1972` n `12`; crypto_alt avg `2.1214` n `234`; crypto_major avg `1.3077` n `8`; equity avg `0.6763` n `141`; fx avg `-0.0469` n `6`; index avg `0.0943` n `26`; metal avg `0.0062` n `20`; unknown avg `14.9274` n `937`
- 24h: commodity avg `-0.1754` n `12`; crypto_alt avg `1.4422` n `234`; crypto_major avg `1.2876` n `8`; equity avg `-0.6038` n `141`; fx avg `-0.1468` n `6`; index avg `-0.0466` n `26`; metal avg `-0.1874` n `20`; unknown avg `61.1236` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1787`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
