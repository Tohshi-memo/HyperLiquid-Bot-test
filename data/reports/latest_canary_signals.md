# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T17:22:18.818849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0204` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0136` n `12`; crypto_alt avg `-0.2366` n `228`; crypto_major avg `-0.1576` n `8`; equity avg `-0.0342` n `74`; fx avg `-0.0008` n `6`; index avg `-0.053` n `23`; metal avg `0.0205` n `18`; unknown avg `-0.1259` n `515`
- 1h: commodity avg `0.0834` n `12`; crypto_alt avg `-0.2535` n `228`; crypto_major avg `-0.1559` n `8`; equity avg `0.0247` n `74`; fx avg `0.017` n `6`; index avg `-0.0273` n `23`; metal avg `0.0378` n `18`; unknown avg `-0.6926` n `515`
- 4h: commodity avg `0.1463` n `12`; crypto_alt avg `-0.918` n `228`; crypto_major avg `-0.9538` n `8`; equity avg `-0.1655` n `74`; fx avg `0.0569` n `6`; index avg `0.0666` n `23`; metal avg `-0.1601` n `18`; unknown avg `-0.6841` n `513`
- 24h: commodity avg `0.5724` n `12`; crypto_alt avg `-2.1885` n `228`; crypto_major avg `-1.6772` n `8`; equity avg `-1.9533` n `74`; fx avg `-0.0077` n `6`; index avg `-0.9662` n `23`; metal avg `-1.2705` n `18`; unknown avg `-0.4796` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
