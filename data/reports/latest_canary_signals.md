# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T11:22:24.783929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0715` n `13`; crypto_alt avg `0.1513` n `235`; crypto_major avg `0.079` n `8`; equity avg `0.1109` n `144`; fx avg `0.0374` n `6`; index avg `0.0247` n `26`; metal avg `0.0309` n `20`; unknown avg `-0.218` n `1079`
- 1h: commodity avg `-0.1238` n `13`; crypto_alt avg `-0.0113` n `235`; crypto_major avg `0.0211` n `8`; equity avg `0.0068` n `144`; fx avg `0.0093` n `6`; index avg `0.0384` n `26`; metal avg `0.0713` n `20`; unknown avg `-0.1186` n `1077`
- 4h: commodity avg `0.0036` n `13`; crypto_alt avg `-0.0967` n `235`; crypto_major avg `-0.0668` n `8`; equity avg `-0.1317` n `144`; fx avg `0.0596` n `6`; index avg `-0.0008` n `26`; metal avg `0.1163` n `20`; unknown avg `25.1549` n `997`
- 24h: commodity avg `-0.2665` n `13`; crypto_alt avg `0.9955` n `235`; crypto_major avg `0.9816` n `8`; equity avg `0.1012` n `144`; fx avg `-0.0473` n `6`; index avg `-0.0572` n `26`; metal avg `0.2988` n `20`; unknown avg `0.5321` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2129`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1952`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
