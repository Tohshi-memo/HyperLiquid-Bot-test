# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T18:52:23.647018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0067` n `12`; crypto_alt avg `-0.1171` n `228`; crypto_major avg `-0.2072` n `8`; equity avg `-0.1412` n `66`; fx avg `0.0001` n `6`; index avg `0.0351` n `23`; metal avg `-0.0387` n `18`; unknown avg `0.0511` n `384`
- 1h: commodity avg `0.2174` n `12`; crypto_alt avg `-0.3232` n `228`; crypto_major avg `-0.4599` n `8`; equity avg `-0.0297` n `66`; fx avg `0.015` n `6`; index avg `0.0923` n `23`; metal avg `0.1757` n `18`; unknown avg `0.0221` n `384`
- 4h: commodity avg `-0.8482` n `12`; crypto_alt avg `0.432` n `228`; crypto_major avg `-0.0974` n `8`; equity avg `0.4097` n `66`; fx avg `0.0483` n `6`; index avg `0.1858` n `23`; metal avg `0.2624` n `18`; unknown avg `0.6811` n `384`
- 24h: commodity avg `-2.7535` n `12`; crypto_alt avg `2.2967` n `228`; crypto_major avg `1.41` n `8`; equity avg `1.1683` n `66`; fx avg `-0.0226` n `6`; index avg `0.9095` n `23`; metal avg `1.3647` n `18`; unknown avg `0.9858` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.044`, n `668`, weak_sample_signal
