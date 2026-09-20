# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T03:52:32.266067+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5622` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5148` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0352` n `12`; crypto_alt avg `0.2692` n `234`; crypto_major avg `0.1628` n `8`; equity avg `0.0644` n `140`; fx avg `-0.0053` n `6`; index avg `-0.0003` n `26`; metal avg `0.0056` n `20`; unknown avg `2.3653` n `943`
- 1h: commodity avg `-0.0185` n `12`; crypto_alt avg `-0.012` n `234`; crypto_major avg `-0.0886` n `8`; equity avg `-0.0969` n `140`; fx avg `-0.0045` n `6`; index avg `-0.035` n `26`; metal avg `-0.0156` n `20`; unknown avg `3.6159` n `941`
- 4h: commodity avg `0.2395` n `12`; crypto_alt avg `-1.4264` n `234`; crypto_major avg `-1.5862` n `8`; equity avg `-0.3217` n `140`; fx avg `0.0108` n `6`; index avg `-0.0714` n `26`; metal avg `-0.024` n `20`; unknown avg `2.4497` n `935`
- 24h: commodity avg `0.1927` n `12`; crypto_alt avg `-0.8666` n `234`; crypto_major avg `-2.0097` n `8`; equity avg `-0.22` n `140`; fx avg `-0.066` n `6`; index avg `-0.0503` n `26`; metal avg `-0.0071` n `20`; unknown avg `1.3279` n `822`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
