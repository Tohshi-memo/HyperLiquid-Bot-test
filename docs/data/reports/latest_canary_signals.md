# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T18:37:30.496001+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0799` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0318` n `12`; crypto_alt avg `-0.0056` n `232`; crypto_major avg `-0.1575` n `8`; equity avg `0.017` n `133`; fx avg `0.0081` n `6`; index avg `0.0025` n `26`; metal avg `-0.0275` n `20`; unknown avg `-0.4408` n `792`
- 1h: commodity avg `-0.0541` n `12`; crypto_alt avg `0.2304` n `232`; crypto_major avg `-0.2341` n `8`; equity avg `0.144` n `133`; fx avg `0.0075` n `6`; index avg `0.0393` n `26`; metal avg `-0.0632` n `20`; unknown avg `-0.3358` n `790`
- 4h: commodity avg `-0.3279` n `12`; crypto_alt avg `2.0566` n `232`; crypto_major avg `1.752` n `8`; equity avg `1.306` n `133`; fx avg `0.0481` n `6`; index avg `0.2615` n `26`; metal avg `0.317` n `20`; unknown avg `1.3287` n `790`
- 24h: commodity avg `-0.0541` n `12`; crypto_alt avg `4.4783` n `232`; crypto_major avg `5.1385` n `8`; equity avg `1.669` n `133`; fx avg `-0.2495` n `6`; index avg `0.218` n `26`; metal avg `0.8699` n `20`; unknown avg `0.9505` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
