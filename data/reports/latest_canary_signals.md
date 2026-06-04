# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T02:37:21.699301+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.9795` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.4608` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.2926` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.2656` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0409` n `12`; crypto_alt avg `0.4815` n `228`; crypto_major avg `0.5405` n `8`; equity avg `0.2456` n `73`; fx avg `0.0176` n `6`; index avg `0.0211` n `23`; metal avg `-0.0352` n `18`; unknown avg `-0.0193` n `420`
- 1h: commodity avg `0.0066` n `12`; crypto_alt avg `-1.8245` n `228`; crypto_major avg `-0.2296` n `8`; equity avg `-0.2775` n `73`; fx avg `0.002` n `6`; index avg `-0.2835` n `23`; metal avg `-0.2728` n `18`; unknown avg `-0.1883` n `420`
- 4h: commodity avg `-0.3564` n `12`; crypto_alt avg `-4.6006` n `228`; crypto_major avg `-2.649` n `8`; equity avg `-0.3834` n `73`; fx avg `-0.0144` n `6`; index avg `-0.1882` n `23`; metal avg `0.3305` n `18`; unknown avg `-0.9891` n `419`
- 24h: commodity avg `0.0494` n `12`; crypto_alt avg `-2.9572` n `228`; crypto_major avg `-3.1202` n `8`; equity avg `-3.7952` n `73`; fx avg `0.0181` n `6`; index avg `-1.3356` n `23`; metal avg `-1.6827` n `18`; unknown avg `0.094` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
