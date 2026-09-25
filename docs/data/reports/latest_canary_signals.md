# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T00:07:29.610586+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0299` n `12`; crypto_alt avg `0.2583` n `234`; crypto_major avg `0.2152` n `8`; equity avg `0.0247` n `141`; fx avg `-0.0126` n `6`; index avg `0.0168` n `26`; metal avg `-0.0094` n `20`; unknown avg `-0.0594` n `938`
- 1h: commodity avg `-0.0894` n `12`; crypto_alt avg `0.1814` n `234`; crypto_major avg `0.2207` n `8`; equity avg `-0.042` n `141`; fx avg `-0.0114` n `6`; index avg `0.0152` n `26`; metal avg `-0.0481` n `20`; unknown avg `2.8367` n `938`
- 4h: commodity avg `-0.416` n `12`; crypto_alt avg `0.1724` n `234`; crypto_major avg `-0.1142` n `8`; equity avg `0.0368` n `141`; fx avg `-0.0202` n `6`; index avg `-0.0025` n `26`; metal avg `-0.0584` n `20`; unknown avg `8.4426` n `860`
- 24h: commodity avg `0.5474` n `12`; crypto_alt avg `3.8428` n `234`; crypto_major avg `0.9312` n `8`; equity avg `-0.2407` n `141`; fx avg `0.0298` n `6`; index avg `-0.078` n `26`; metal avg `-0.1087` n `20`; unknown avg `24.6218` n `815`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
