# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T23:52:36.644487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `12`; crypto_alt avg `0.1422` n `234`; crypto_major avg `0.1758` n `8`; equity avg `0.0326` n `140`; fx avg `-0.0211` n `6`; index avg `0.0028` n `26`; metal avg `-0.0188` n `20`; unknown avg `0.4818` n `945`
- 1h: commodity avg `0.0061` n `12`; crypto_alt avg `0.3822` n `234`; crypto_major avg `-0.0182` n `8`; equity avg `0.109` n `140`; fx avg `-0.0573` n `6`; index avg `0.0105` n `26`; metal avg `0.0145` n `20`; unknown avg `1.4729` n `943`
- 4h: commodity avg `0.1004` n `12`; crypto_alt avg `1.471` n `234`; crypto_major avg `0.2347` n `8`; equity avg `0.1028` n `140`; fx avg `-0.0656` n `6`; index avg `-0.0232` n `26`; metal avg `-0.052` n `20`; unknown avg `1.4309` n `906`
- 24h: commodity avg `0.1083` n `12`; crypto_alt avg `3.1102` n `234`; crypto_major avg `0.63` n `8`; equity avg `0.7515` n `140`; fx avg `-0.3308` n `6`; index avg `0.1067` n `26`; metal avg `0.1728` n `20`; unknown avg `0.9877` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
