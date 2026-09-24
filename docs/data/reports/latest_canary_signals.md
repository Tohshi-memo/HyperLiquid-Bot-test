# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T04:22:30.860827+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0269` n `12`; crypto_alt avg `-0.0715` n `234`; crypto_major avg `-0.0637` n `8`; equity avg `-0.0067` n `141`; fx avg `0.0064` n `6`; index avg `0.0033` n `26`; metal avg `0.0199` n `20`; unknown avg `1.2537` n `945`
- 1h: commodity avg `0.0581` n `12`; crypto_alt avg `-0.3218` n `234`; crypto_major avg `-0.3092` n `8`; equity avg `-0.3333` n `141`; fx avg `0.0021` n `6`; index avg `-0.0338` n `26`; metal avg `-0.0048` n `20`; unknown avg `-0.0411` n `937`
- 4h: commodity avg `0.0056` n `12`; crypto_alt avg `0.5096` n `234`; crypto_major avg `-0.595` n `8`; equity avg `-0.4788` n `141`; fx avg `0.039` n `6`; index avg `-0.0552` n `26`; metal avg `0.0481` n `20`; unknown avg `2.0304` n `937`
- 24h: commodity avg `0.5803` n `12`; crypto_alt avg `-4.7123` n `234`; crypto_major avg `-5.0983` n `8`; equity avg `-2.0626` n `140`; fx avg `0.1143` n `6`; index avg `-0.3863` n `26`; metal avg `-0.6724` n `20`; unknown avg `585.0859` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
