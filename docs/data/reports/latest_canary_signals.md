# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T15:22:15.126126+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1062` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.2306` n `12`; crypto_alt avg `-0.0532` n `228`; crypto_major avg `0.0267` n `8`; equity avg `0.0202` n `67`; fx avg `-0.001` n `6`; index avg `-0.084` n `23`; metal avg `0.0519` n `18`; unknown avg `0.0966` n `396`
- 1h: commodity avg `-0.1368` n `12`; crypto_alt avg `0.8817` n `228`; crypto_major avg `0.8836` n `8`; equity avg `0.485` n `67`; fx avg `-0.0016` n `6`; index avg `0.1428` n `23`; metal avg `0.1473` n `18`; unknown avg `0.7739` n `396`
- 4h: commodity avg `-0.5673` n `12`; crypto_alt avg `1.9449` n `228`; crypto_major avg `1.5389` n `8`; equity avg `0.7822` n `67`; fx avg `-0.0116` n `6`; index avg `0.4696` n `23`; metal avg `0.22` n `18`; unknown avg `1.3976` n `396`
- 24h: commodity avg `-0.094` n `12`; crypto_alt avg `-3.0657` n `228`; crypto_major avg `-2.0925` n `8`; equity avg `-0.9007` n `67`; fx avg `0.0481` n `6`; index avg `-0.0695` n `23`; metal avg `-0.0667` n `18`; unknown avg `-2.1519` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
