# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T16:22:32.890122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0493` n `13`; crypto_alt avg `-0.0776` n `235`; crypto_major avg `-0.0312` n `8`; equity avg `-0.0604` n `150`; fx avg `-0.0095` n `6`; index avg `0.0016` n `26`; metal avg `0.0024` n `20`; unknown avg `-0.1767` n `1076`
- 1h: commodity avg `-0.3389` n `13`; crypto_alt avg `1.1653` n `235`; crypto_major avg `0.6994` n `8`; equity avg `0.226` n `150`; fx avg `-0.0068` n `6`; index avg `0.065` n `26`; metal avg `0.1271` n `20`; unknown avg `0.5069` n `1068`
- 4h: commodity avg `-0.1904` n `13`; crypto_alt avg `0.1657` n `235`; crypto_major avg `-0.0305` n `8`; equity avg `0.2121` n `150`; fx avg `0.0191` n `6`; index avg `0.0472` n `26`; metal avg `-0.0005` n `20`; unknown avg `0.006` n `1022`
- 24h: commodity avg `0.728` n `13`; crypto_alt avg `-4.7924` n `235`; crypto_major avg `-3.2871` n `8`; equity avg `-1.5996` n `150`; fx avg `-0.1587` n `6`; index avg `-0.3067` n `26`; metal avg `-0.5637` n `20`; unknown avg `15.6496` n `988`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
