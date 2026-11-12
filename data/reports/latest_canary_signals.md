# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T22:22:37.282477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `13`; crypto_alt avg `-0.1613` n `239`; crypto_major avg `-0.126` n `8`; equity avg `-0.1334` n `162`; fx avg `-0.0027` n `6`; index avg `-0.0179` n `27`; metal avg `-0.0118` n `20`; unknown avg `4.0538` n `1259`
- 1h: commodity avg `-0.0778` n `13`; crypto_alt avg `0.0187` n `239`; crypto_major avg `-0.0931` n `8`; equity avg `0.026` n `162`; fx avg `-0.015` n `6`; index avg `-0.0063` n `27`; metal avg `0.032` n `20`; unknown avg `11.0816` n `1251`
- 4h: commodity avg `0.2611` n `13`; crypto_alt avg `0.6473` n `239`; crypto_major avg `0.037` n `8`; equity avg `-0.3802` n `162`; fx avg `0.0011` n `6`; index avg `-0.0349` n `27`; metal avg `-0.062` n `20`; unknown avg `0.0677` n `1219`
- 24h: commodity avg `0.8653` n `13`; crypto_alt avg `-2.0965` n `239`; crypto_major avg `-2.8965` n `8`; equity avg `-1.967` n `162`; fx avg `-0.1365` n `6`; index avg `-0.0884` n `27`; metal avg `-0.7303` n `20`; unknown avg `49.8225` n `1151`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
