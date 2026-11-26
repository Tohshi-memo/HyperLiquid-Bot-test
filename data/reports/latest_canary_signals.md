# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T10:52:42.977874+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.074` n `13`; crypto_alt avg `-0.2567` n `239`; crypto_major avg `-0.3751` n `8`; equity avg `-0.2013` n `168`; fx avg `-0.0081` n `6`; index avg `-0.0259` n `27`; metal avg `-0.029` n `20`; unknown avg `0.5992` n `1267`
- 1h: commodity avg `0.0899` n `13`; crypto_alt avg `-0.2535` n `239`; crypto_major avg `-0.6457` n `8`; equity avg `-0.3403` n `168`; fx avg `0.0061` n `6`; index avg `-0.0376` n `27`; metal avg `-0.1614` n `20`; unknown avg `1.1415` n `1259`
- 4h: commodity avg `0.1301` n `13`; crypto_alt avg `0.2256` n `239`; crypto_major avg `-0.1346` n `8`; equity avg `-0.2003` n `168`; fx avg `0.0563` n `6`; index avg `-0.0212` n `27`; metal avg `0.0006` n `20`; unknown avg `175.8945` n `1151`
- 24h: commodity avg `0.562` n `13`; crypto_alt avg `3.5903` n `239`; crypto_major avg `3.1474` n `8`; equity avg `3.5386` n `168`; fx avg `0.0893` n `6`; index avg `0.3016` n `27`; metal avg `0.6406` n `20`; unknown avg `200.5816` n `999`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
