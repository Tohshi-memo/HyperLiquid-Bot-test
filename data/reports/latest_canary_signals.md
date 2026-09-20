# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T18:52:36.746030+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `12`; crypto_alt avg `-0.3292` n `234`; crypto_major avg `-0.2216` n `8`; equity avg `-0.0225` n `140`; fx avg `0.001` n `6`; index avg `0.0021` n `26`; metal avg `-0.0005` n `20`; unknown avg `0.9478` n `943`
- 1h: commodity avg `-0.0127` n `12`; crypto_alt avg `-0.461` n `234`; crypto_major avg `-0.2014` n `8`; equity avg `-0.0697` n `140`; fx avg `0.0066` n `6`; index avg `0.0005` n `26`; metal avg `-0.0357` n `20`; unknown avg `33.6293` n `933`
- 4h: commodity avg `-0.0191` n `12`; crypto_alt avg `2.119` n `234`; crypto_major avg `1.2566` n `8`; equity avg `0.2349` n `140`; fx avg `-0.0059` n `6`; index avg `0.0317` n `26`; metal avg `-0.0115` n `20`; unknown avg `1.6443` n `871`
- 24h: commodity avg `0.3685` n `12`; crypto_alt avg `-0.0492` n `234`; crypto_major avg `-0.8085` n `8`; equity avg `-0.1263` n `140`; fx avg `-0.0246` n `6`; index avg `-0.0385` n `26`; metal avg `-0.0436` n `20`; unknown avg `62.7542` n `819`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
