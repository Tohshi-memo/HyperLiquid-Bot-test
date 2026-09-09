# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T17:52:34.211130+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.038` n `12`; crypto_alt avg `-0.0671` n `233`; crypto_major avg `-0.0425` n `8`; equity avg `0.1008` n `134`; fx avg `-0.0065` n `6`; index avg `0.0135` n `26`; metal avg `-0.007` n `20`; unknown avg `8.3832` n `797`
- 1h: commodity avg `-0.0629` n `12`; crypto_alt avg `0.0323` n `233`; crypto_major avg `0.1579` n `8`; equity avg `-0.0093` n `134`; fx avg `0.0294` n `6`; index avg `0.0067` n `26`; metal avg `0.0386` n `20`; unknown avg `0.1445` n `795`
- 4h: commodity avg `-0.0683` n `12`; crypto_alt avg `-0.616` n `233`; crypto_major avg `-0.6621` n `8`; equity avg `-0.2752` n `134`; fx avg `0.0478` n `6`; index avg `-0.0834` n `26`; metal avg `0.0584` n `20`; unknown avg `5.1975` n `769`
- 24h: commodity avg `0.3601` n `12`; crypto_alt avg `-0.739` n `233`; crypto_major avg `-0.1111` n `8`; equity avg `-0.5977` n `134`; fx avg `-0.0629` n `6`; index avg `-0.2213` n `26`; metal avg `0.4282` n `20`; unknown avg `5.2272` n `699`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
