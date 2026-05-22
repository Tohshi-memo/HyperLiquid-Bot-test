# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T10:37:15.453134+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0455` n `12`; crypto_alt avg `0.2433` n `228`; crypto_major avg `0.1074` n `8`; equity avg `-0.1043` n `67`; fx avg `-0.0042` n `6`; index avg `-0.0866` n `23`; metal avg `-0.2188` n `18`; unknown avg `-0.2493` n `386`
- 1h: commodity avg `0.1386` n `12`; crypto_alt avg `0.0231` n `228`; crypto_major avg `0.0214` n `8`; equity avg `-0.2426` n `67`; fx avg `-0.0115` n `6`; index avg `-0.0967` n `23`; metal avg `0.0805` n `18`; unknown avg `-0.0474` n `386`
- 4h: commodity avg `0.1464` n `12`; crypto_alt avg `0.254` n `228`; crypto_major avg `0.3441` n `8`; equity avg `-0.7406` n `67`; fx avg `-0.0178` n `6`; index avg `-0.2056` n `23`; metal avg `-0.0096` n `18`; unknown avg `-0.2373` n `386`
- 24h: commodity avg `-0.6762` n `12`; crypto_alt avg `2.1984` n `228`; crypto_major avg `0.5347` n `8`; equity avg `0.8741` n `67`; fx avg `0.079` n `6`; index avg `0.6098` n `23`; metal avg `0.854` n `18`; unknown avg `0.9364` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0464`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0404`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0397`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.039`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.036`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0336`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0331`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0324`, n `668`, weak_sample_signal
