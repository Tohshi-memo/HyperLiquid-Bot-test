# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T01:37:27.942743+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0217` n `12`; crypto_alt avg `0.0678` n `232`; crypto_major avg `0.0101` n `8`; equity avg `0.0454` n `134`; fx avg `-0.0211` n `6`; index avg `0.0121` n `26`; metal avg `0.0206` n `20`; unknown avg `-0.0914` n `797`
- 1h: commodity avg `-0.0511` n `12`; crypto_alt avg `0.5156` n `232`; crypto_major avg `0.2168` n `8`; equity avg `0.1132` n `134`; fx avg `-0.0432` n `6`; index avg `0.0333` n `26`; metal avg `0.0789` n `20`; unknown avg `0.8496` n `795`
- 4h: commodity avg `-0.0591` n `12`; crypto_alt avg `0.5972` n `232`; crypto_major avg `0.3099` n `8`; equity avg `0.2172` n `134`; fx avg `-0.1584` n `6`; index avg `0.0453` n `26`; metal avg `0.1999` n `20`; unknown avg `13.4625` n `788`
- 24h: commodity avg `0.1229` n `12`; crypto_alt avg `1.1719` n `232`; crypto_major avg `-0.5042` n `8`; equity avg `0.7412` n `134`; fx avg `-0.2283` n `6`; index avg `0.126` n `26`; metal avg `0.2997` n `20`; unknown avg `7766.9917` n `644`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
