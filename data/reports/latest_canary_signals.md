# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T08:22:39.274879+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0405` n `13`; crypto_alt avg `-0.189` n `239`; crypto_major avg `-0.1814` n `8`; equity avg `0.0364` n `162`; fx avg `0.0082` n `6`; index avg `0.0063` n `27`; metal avg `0.0087` n `20`; unknown avg `1.1754` n `1265`
- 1h: commodity avg `-0.0184` n `13`; crypto_alt avg `-0.0466` n `239`; crypto_major avg `-0.0186` n `8`; equity avg `0.2641` n `162`; fx avg `0.0026` n `6`; index avg `0.0559` n `27`; metal avg `0.0067` n `20`; unknown avg `1.8531` n `1219`
- 4h: commodity avg `0.0569` n `13`; crypto_alt avg `-0.9623` n `239`; crypto_major avg `-0.6664` n `8`; equity avg `-0.5422` n `162`; fx avg `-0.0154` n `6`; index avg `-0.0212` n `27`; metal avg `-0.0407` n `20`; unknown avg `47.3938` n `1077`
- 24h: commodity avg `-0.2249` n `13`; crypto_alt avg `0.259` n `239`; crypto_major avg `0.828` n `8`; equity avg `-0.1095` n `162`; fx avg `-0.0484` n `6`; index avg `0.031` n `27`; metal avg `0.0926` n `20`; unknown avg `1.588` n `1051`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
