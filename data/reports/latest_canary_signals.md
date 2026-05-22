# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T17:37:15.487724+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0663` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.5163` n `12`; crypto_alt avg `0.3784` n `228`; crypto_major avg `0.2291` n `8`; equity avg `0.1929` n `67`; fx avg `-0.0057` n `6`; index avg `0.1034` n `23`; metal avg `0.0605` n `18`; unknown avg `0.2364` n `386`
- 1h: commodity avg `-0.4119` n `12`; crypto_alt avg `0.4561` n `228`; crypto_major avg `0.1924` n `8`; equity avg `0.1352` n `67`; fx avg `-0.0026` n `6`; index avg `0.1142` n `23`; metal avg `-0.0137` n `18`; unknown avg `0.1002` n `386`
- 4h: commodity avg `-0.7869` n `12`; crypto_alt avg `-0.8511` n `228`; crypto_major avg `-0.8736` n `8`; equity avg `-0.4927` n `67`; fx avg `0.0536` n `6`; index avg `0.1927` n `23`; metal avg `-0.0854` n `18`; unknown avg `-0.6331` n `386`
- 24h: commodity avg `-1.5277` n `12`; crypto_alt avg `0.1078` n `228`; crypto_major avg `-0.9301` n `8`; equity avg `0.1397` n `67`; fx avg `0.1784` n `6`; index avg `0.8923` n `23`; metal avg `-0.7753` n `18`; unknown avg `-1.1887` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0481`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.043`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0422`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0417`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.041`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0407`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0396`, n `668`, weak_sample_signal
