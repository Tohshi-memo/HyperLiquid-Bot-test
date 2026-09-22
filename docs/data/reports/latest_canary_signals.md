# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T13:37:32.896603+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1101` n `12`; crypto_alt avg `-0.4425` n `234`; crypto_major avg `-0.1226` n `8`; equity avg `0.6573` n `140`; fx avg `-0.0015` n `6`; index avg `0.0624` n `26`; metal avg `-0.0557` n `20`; unknown avg `53.0598` n `942`
- 1h: commodity avg `0.0782` n `12`; crypto_alt avg `0.2534` n `234`; crypto_major avg `0.0562` n `8`; equity avg `0.5668` n `140`; fx avg `0.0069` n `6`; index avg `0.0667` n `26`; metal avg `0.0288` n `20`; unknown avg `531.5082` n `940`
- 4h: commodity avg `-0.0481` n `12`; crypto_alt avg `0.123` n `234`; crypto_major avg `0.235` n `8`; equity avg `0.7367` n `140`; fx avg `0.038` n `6`; index avg `0.1103` n `26`; metal avg `0.2468` n `20`; unknown avg `3.0852` n `932`
- 24h: commodity avg `-0.3488` n `12`; crypto_alt avg `0.9907` n `234`; crypto_major avg `1.8399` n `8`; equity avg `1.4765` n `140`; fx avg `-0.2403` n `6`; index avg `0.3095` n `26`; metal avg `-0.106` n `20`; unknown avg `1105.5732` n `802`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
