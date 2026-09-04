# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T10:07:26.637944+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0232` n `12`; crypto_alt avg `-0.0966` n `232`; crypto_major avg `0.0282` n `8`; equity avg `0.0539` n `133`; fx avg `-0.0135` n `6`; index avg `0.0055` n `26`; metal avg `-0.0066` n `20`; unknown avg `0.0086` n `791`
- 1h: commodity avg `0.0181` n `12`; crypto_alt avg `-0.0785` n `232`; crypto_major avg `-0.1807` n `8`; equity avg `0.0892` n `133`; fx avg `-0.0128` n `6`; index avg `0.0039` n `26`; metal avg `-0.0817` n `20`; unknown avg `-0.067` n `791`
- 4h: commodity avg `-0.0226` n `12`; crypto_alt avg `0.9572` n `232`; crypto_major avg `0.146` n `8`; equity avg `0.2573` n `133`; fx avg `-0.0063` n `6`; index avg `0.0122` n `26`; metal avg `-0.0163` n `20`; unknown avg `-0.2299` n `783`
- 24h: commodity avg `-0.3941` n `12`; crypto_alt avg `2.714` n `232`; crypto_major avg `4.2056` n `8`; equity avg `2.3258` n `133`; fx avg `-0.0111` n `6`; index avg `0.4185` n `26`; metal avg `0.451` n `20`; unknown avg `1.815` n `730`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
