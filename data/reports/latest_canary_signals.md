# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T00:22:31.550405+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0202` n `12`; crypto_alt avg `-0.0279` n `234`; crypto_major avg `0.0336` n `8`; equity avg `0.1304` n `141`; fx avg `0.0051` n `6`; index avg `0.0093` n `26`; metal avg `-0.0124` n `20`; unknown avg `0.1688` n `946`
- 1h: commodity avg `-0.0603` n `12`; crypto_alt avg `0.253` n `234`; crypto_major avg `0.278` n `8`; equity avg `0.1169` n `141`; fx avg `-0.0201` n `6`; index avg `0.0273` n `26`; metal avg `-0.0481` n `20`; unknown avg `1.7035` n `938`
- 4h: commodity avg `-0.3597` n `12`; crypto_alt avg `0.2584` n `234`; crypto_major avg `0.0325` n `8`; equity avg `0.277` n `141`; fx avg `-0.0078` n `6`; index avg `0.0403` n `26`; metal avg `-0.0028` n `20`; unknown avg `4.3422` n `892`
- 24h: commodity avg `0.5748` n `12`; crypto_alt avg `4.0179` n `234`; crypto_major avg `1.04` n `8`; equity avg `-0.0875` n `141`; fx avg `0.0338` n `6`; index avg `-0.0689` n `26`; metal avg `-0.0627` n `20`; unknown avg `22.2441` n `815`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
