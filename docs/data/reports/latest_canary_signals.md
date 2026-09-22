# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T17:52:33.613106+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0945` n `12`; crypto_alt avg `0.1906` n `234`; crypto_major avg `0.0714` n `8`; equity avg `0.1825` n `140`; fx avg `-0.0015` n `6`; index avg `0.043` n `26`; metal avg `0.0934` n `20`; unknown avg `0.5695` n `942`
- 1h: commodity avg `-0.1641` n `12`; crypto_alt avg `0.5196` n `234`; crypto_major avg `0.2968` n `8`; equity avg `0.286` n `140`; fx avg `0.0078` n `6`; index avg `0.0377` n `26`; metal avg `0.0883` n `20`; unknown avg `0.6787` n `940`
- 4h: commodity avg `0.2028` n `12`; crypto_alt avg `0.8666` n `234`; crypto_major avg `0.1882` n `8`; equity avg `0.1255` n `140`; fx avg `-0.0129` n `6`; index avg `0.0258` n `26`; metal avg `0.0273` n `20`; unknown avg `0.6263` n `880`
- 24h: commodity avg `0.0582` n `12`; crypto_alt avg `2.9082` n `234`; crypto_major avg `1.7266` n `8`; equity avg `0.9567` n `140`; fx avg `-0.2815` n `6`; index avg `0.1343` n `26`; metal avg `0.1709` n `20`; unknown avg `0.4557` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
