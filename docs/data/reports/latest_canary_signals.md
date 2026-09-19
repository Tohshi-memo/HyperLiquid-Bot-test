# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T14:07:28.375363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `12`; crypto_alt avg `0.1864` n `234`; crypto_major avg `0.1885` n `8`; equity avg `0.0167` n `140`; fx avg `0.0009` n `6`; index avg `0.0022` n `26`; metal avg `0.0062` n `20`; unknown avg `-0.2479` n `940`
- 1h: commodity avg `-0.0047` n `12`; crypto_alt avg `0.0976` n `234`; crypto_major avg `0.1096` n `8`; equity avg `0.0474` n `140`; fx avg `0.0039` n `6`; index avg `0.0034` n `26`; metal avg `0.007` n `20`; unknown avg `-0.0416` n `938`
- 4h: commodity avg `0.0078` n `12`; crypto_alt avg `0.6723` n `234`; crypto_major avg `0.6704` n `8`; equity avg `0.0562` n `140`; fx avg `-0.0279` n `6`; index avg `0.0024` n `26`; metal avg `0.0286` n `20`; unknown avg `0.3053` n `932`
- 24h: commodity avg `-0.1966` n `12`; crypto_alt avg `3.4603` n `234`; crypto_major avg `2.3063` n `8`; equity avg `1.1304` n `140`; fx avg `-0.0222` n `6`; index avg `0.1423` n `26`; metal avg `0.1279` n `20`; unknown avg `1.6445` n `806`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1695`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
