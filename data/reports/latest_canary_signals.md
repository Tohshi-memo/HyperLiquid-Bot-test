# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T17:22:27.254837+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5683` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0131` n `12`; crypto_alt avg `-0.0611` n `234`; crypto_major avg `-0.1797` n `8`; equity avg `0.0186` n `140`; fx avg `0.0111` n `6`; index avg `-0.0037` n `26`; metal avg `0.0002` n `20`; unknown avg `16.9543` n `931`
- 1h: commodity avg `0.006` n `12`; crypto_alt avg `1.0617` n `234`; crypto_major avg `0.5043` n `8`; equity avg `0.0713` n `140`; fx avg `0.0081` n `6`; index avg `0.0085` n `26`; metal avg `0.004` n `20`; unknown avg `16.6603` n `929`
- 4h: commodity avg `-0.0216` n `12`; crypto_alt avg `2.6481` n `234`; crypto_major avg `1.5915` n `8`; equity avg `0.303` n `140`; fx avg `0.0306` n `6`; index avg `0.0291` n `26`; metal avg `0.0232` n `20`; unknown avg `1.529` n `879`
- 24h: commodity avg `0.3983` n `12`; crypto_alt avg `-0.2966` n `234`; crypto_major avg `-1.1108` n `8`; equity avg `-0.0135` n `140`; fx avg `-0.0165` n `6`; index avg `-0.029` n `26`; metal avg `0.0018` n `20`; unknown avg `168.6266` n `827`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
