# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T11:07:26.390539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0902` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0445` n `12`; crypto_alt avg `-0.71` n `233`; crypto_major avg `-0.5097` n `8`; equity avg `-0.1531` n `136`; fx avg `-0.0305` n `6`; index avg `-0.0201` n `26`; metal avg `-0.0383` n `20`; unknown avg `-0.1137` n `794`
- 1h: commodity avg `-0.0661` n `12`; crypto_alt avg `-1.3304` n `233`; crypto_major avg `-0.7874` n `8`; equity avg `-0.2913` n `136`; fx avg `-0.0484` n `6`; index avg `-0.0472` n `26`; metal avg `-0.0687` n `20`; unknown avg `-0.2412` n `794`
- 4h: commodity avg `-0.3316` n `12`; crypto_alt avg `-1.7686` n `233`; crypto_major avg `-1.0767` n `8`; equity avg `-0.1173` n `136`; fx avg `-0.1064` n `6`; index avg `0.0135` n `26`; metal avg `-0.0736` n `20`; unknown avg `-0.455` n `786`
- 24h: commodity avg `0.2152` n `12`; crypto_alt avg `-2.3502` n `233`; crypto_major avg `-1.9343` n `8`; equity avg `-0.912` n `136`; fx avg `-0.1186` n `6`; index avg `-0.092` n `26`; metal avg `-0.4611` n `20`; unknown avg `1.0515` n `683`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
