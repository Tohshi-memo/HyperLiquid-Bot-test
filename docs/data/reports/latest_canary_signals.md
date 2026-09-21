# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T12:52:31.437220+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0121` n `12`; crypto_alt avg `-0.0967` n `234`; crypto_major avg `-0.1896` n `8`; equity avg `0.0298` n `140`; fx avg `-0.0134` n `6`; index avg `0.0079` n `26`; metal avg `0.0502` n `20`; unknown avg `-0.0668` n `944`
- 1h: commodity avg `0.0206` n `12`; crypto_alt avg `0.2588` n `234`; crypto_major avg `0.0214` n `8`; equity avg `0.067` n `140`; fx avg `-0.0029` n `6`; index avg `0.0042` n `26`; metal avg `0.0526` n `20`; unknown avg `1.0944` n `934`
- 4h: commodity avg `-0.1895` n `12`; crypto_alt avg `1.2604` n `234`; crypto_major avg `0.7476` n `8`; equity avg `0.1821` n `140`; fx avg `0.0347` n `6`; index avg `0.037` n `26`; metal avg `0.1941` n `20`; unknown avg `0.2177` n `910`
- 24h: commodity avg `-0.8274` n `12`; crypto_alt avg `7.1654` n `234`; crypto_major avg `5.9101` n `8`; equity avg `2.1088` n `140`; fx avg `-0.0652` n `6`; index avg `0.3852` n `26`; metal avg `0.249` n `20`; unknown avg `4.028` n `733`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1954`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
