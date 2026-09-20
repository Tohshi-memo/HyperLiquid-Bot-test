# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T17:07:29.847081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5945` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0297` n `12`; crypto_alt avg `0.0436` n `234`; crypto_major avg `0.0047` n `8`; equity avg `0.023` n `140`; fx avg `-0.0172` n `6`; index avg `0.0018` n `26`; metal avg `-0.0126` n `20`; unknown avg `0.3547` n `941`
- 1h: commodity avg `-0.004` n `12`; crypto_alt avg `1.4905` n `234`; crypto_major avg `0.9204` n `8`; equity avg `0.121` n `140`; fx avg `0.0146` n `6`; index avg `0.0322` n `26`; metal avg `0.0179` n `20`; unknown avg `5.9542` n `933`
- 4h: commodity avg `-0.0324` n `12`; crypto_alt avg `2.4188` n `234`; crypto_major avg `1.6202` n `8`; equity avg `0.2777` n `140`; fx avg `0.0142` n `6`; index avg `0.037` n `26`; metal avg `0.0257` n `20`; unknown avg `1.1892` n `889`
- 24h: commodity avg `0.3924` n `12`; crypto_alt avg `-0.298` n `234`; crypto_major avg `-1.1233` n `8`; equity avg `-0.0462` n `140`; fx avg `-0.0271` n `6`; index avg `-0.0244` n `26`; metal avg `-0.0065` n `20`; unknown avg `169.3273` n `827`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
