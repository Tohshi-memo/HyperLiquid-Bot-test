# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T16:20:44.455723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1143` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.2142` n `12`; crypto_alt avg `-0.4349` n `228`; crypto_major avg `-0.4041` n `8`; equity avg `-0.3281` n `66`; fx avg `0.0011` n `6`; index avg `-0.1564` n `23`; metal avg `-0.2147` n `18`; unknown avg `-0.1524` n `384`
- 1h: commodity avg `0.0922` n `12`; crypto_alt avg `-0.2075` n `228`; crypto_major avg `-0.4482` n `8`; equity avg `-0.3173` n `66`; fx avg `0.0241` n `6`; index avg `-0.1318` n `23`; metal avg `-0.3706` n `18`; unknown avg `-0.0059` n `384`
- 4h: commodity avg `-1.3268` n `12`; crypto_alt avg `1.3796` n `228`; crypto_major avg `0.7875` n `8`; equity avg `0.3619` n `66`; fx avg `-0.0031` n `6`; index avg `0.583` n `23`; metal avg `0.5557` n `18`; unknown avg `0.4759` n `384`
- 24h: commodity avg `-2.045` n `12`; crypto_alt avg `2.6194` n `228`; crypto_major avg `1.6435` n `8`; equity avg `1.8685` n `66`; fx avg `0.0161` n `6`; index avg `1.1444` n `23`; metal avg `1.0339` n `18`; unknown avg `1.0868` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0517`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0485`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0459`, n `668`, weak_sample_signal
