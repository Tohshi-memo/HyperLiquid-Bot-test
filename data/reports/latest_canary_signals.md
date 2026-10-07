# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T12:37:28.293948+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.043` n `13`; crypto_alt avg `0.0571` n `235`; crypto_major avg `0.129` n `8`; equity avg `0.0201` n `150`; fx avg `-0.0061` n `6`; index avg `0.0085` n `26`; metal avg `-0.2698` n `20`; unknown avg `0.6625` n `1076`
- 1h: commodity avg `-0.0507` n `13`; crypto_alt avg `0.1045` n `235`; crypto_major avg `0.1144` n `8`; equity avg `-0.104` n `150`; fx avg `-0.0399` n `6`; index avg `-0.0125` n `26`; metal avg `-0.3389` n `20`; unknown avg `0.3179` n `1068`
- 4h: commodity avg `0.2588` n `13`; crypto_alt avg `-1.4572` n `235`; crypto_major avg `-1.0891` n `8`; equity avg `-0.8967` n `150`; fx avg `-0.0562` n `6`; index avg `-0.1615` n `26`; metal avg `-0.5301` n `20`; unknown avg `1.7246` n `1068`
- 24h: commodity avg `1.4104` n `13`; crypto_alt avg `-5.1497` n `235`; crypto_major avg `-3.4883` n `8`; equity avg `-1.6546` n `150`; fx avg `-0.2198` n `6`; index avg `-0.3691` n `26`; metal avg `-0.8005` n `20`; unknown avg `814.4228` n `980`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
