# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T18:37:31.349116+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.0187` n `234`; crypto_major avg `0.0109` n `8`; equity avg `0.0754` n `141`; fx avg `-0.0043` n `6`; index avg `0.005` n `26`; metal avg `0.0107` n `20`; unknown avg `3.4957` n `943`
- 1h: commodity avg `-0.1106` n `12`; crypto_alt avg `-0.2565` n `234`; crypto_major avg `0.1259` n `8`; equity avg `-0.0358` n `141`; fx avg `-0.0046` n `6`; index avg `-0.0099` n `26`; metal avg `0.0689` n `20`; unknown avg `6.4605` n `939`
- 4h: commodity avg `0.4997` n `12`; crypto_alt avg `-0.1318` n `234`; crypto_major avg `0.2606` n `8`; equity avg `0.3106` n `141`; fx avg `0.0086` n `6`; index avg `0.032` n `26`; metal avg `0.0828` n `20`; unknown avg `14.0076` n `881`
- 24h: commodity avg `0.8654` n `12`; crypto_alt avg `3.4418` n `234`; crypto_major avg `1.6971` n `8`; equity avg `-0.4919` n `141`; fx avg `0.0414` n `6`; index avg `-0.1041` n `26`; metal avg `-0.0812` n `20`; unknown avg `264.9926` n `831`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
