# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T10:37:25.342668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0316` n `12`; crypto_alt avg `-0.0259` n `233`; crypto_major avg `0.0738` n `8`; equity avg `0.1099` n `134`; fx avg `-0.0123` n `6`; index avg `0.0031` n `26`; metal avg `0.0152` n `20`; unknown avg `-0.0275` n `798`
- 1h: commodity avg `0.0357` n `12`; crypto_alt avg `-0.4218` n `233`; crypto_major avg `-0.2704` n `8`; equity avg `-0.3161` n `134`; fx avg `0.0091` n `6`; index avg `-0.0777` n `26`; metal avg `0.0007` n `20`; unknown avg `1.1144` n `796`
- 4h: commodity avg `0.1641` n `12`; crypto_alt avg `-0.421` n `233`; crypto_major avg `-0.4199` n `8`; equity avg `-0.5774` n `134`; fx avg `0.0096` n `6`; index avg `-0.1577` n `26`; metal avg `-0.0445` n `20`; unknown avg `0.5131` n `790`
- 24h: commodity avg `0.0418` n `12`; crypto_alt avg `-0.6153` n `232`; crypto_major avg `0.5692` n `8`; equity avg `0.3998` n `134`; fx avg `-0.0918` n `6`; index avg `-0.1503` n `26`; metal avg `-0.0358` n `20`; unknown avg `0.6568` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
