# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T07:37:28.036395+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0177` n `12`; crypto_alt avg `0.2449` n `234`; crypto_major avg `0.1752` n `8`; equity avg `0.0135` n `141`; fx avg `-0.0022` n `6`; index avg `0.0018` n `26`; metal avg `0.0003` n `20`; unknown avg `0.0167` n `961`
- 1h: commodity avg `-0.0447` n `12`; crypto_alt avg `0.4872` n `234`; crypto_major avg `0.2049` n `8`; equity avg `0.0572` n `141`; fx avg `-0.0061` n `6`; index avg `0.0037` n `26`; metal avg `0.0126` n `20`; unknown avg `-0.125` n `959`
- 4h: commodity avg `-0.0066` n `12`; crypto_alt avg `1.0601` n `234`; crypto_major avg `0.5034` n `8`; equity avg `0.0893` n `141`; fx avg `0.007` n `6`; index avg `0.0142` n `26`; metal avg `0.0036` n `20`; unknown avg `27.1983` n `933`
- 24h: commodity avg `-0.006` n `12`; crypto_alt avg `1.0808` n `234`; crypto_major avg `0.338` n `8`; equity avg `0.314` n `141`; fx avg `-0.0031` n `6`; index avg `0.0128` n `26`; metal avg `-0.002` n `20`; unknown avg `4.7896` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
