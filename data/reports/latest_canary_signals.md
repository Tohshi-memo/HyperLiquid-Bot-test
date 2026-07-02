# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T18:37:26.131287+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.3738` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- polymarket_volume_spike: score `2.13` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `-0.0222` n `229`; crypto_major avg `-0.0123` n `8`; equity avg `0.1512` n `88`; fx avg `0.002` n `6`; index avg `0.0338` n `25`; metal avg `0.1145` n `20`; unknown avg `0.1588` n `765`
- 1h: commodity avg `0.0501` n `12`; crypto_alt avg `0.2118` n `229`; crypto_major avg `0.3336` n `8`; equity avg `0.2895` n `88`; fx avg `0.0395` n `6`; index avg `0.071` n `25`; metal avg `0.1797` n `20`; unknown avg `-0.0433` n `765`
- 4h: commodity avg `0.3234` n `12`; crypto_alt avg `-0.0597` n `229`; crypto_major avg `0.1466` n `8`; equity avg `-2.2272` n `88`; fx avg `-0.0783` n `6`; index avg `-0.4102` n `25`; metal avg `-0.0404` n `20`; unknown avg `-0.1668` n `763`
- 24h: commodity avg `-0.0212` n `12`; crypto_alt avg `2.0342` n `228`; crypto_major avg `2.7061` n `8`; equity avg `-3.12` n `88`; fx avg `-0.0945` n `6`; index avg `-0.6421` n `25`; metal avg `0.7512` n `20`; unknown avg `1.5471` n `739`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
