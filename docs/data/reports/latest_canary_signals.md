# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T02:22:29.070639+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0061` n `12`; crypto_alt avg `0.3733` n `232`; crypto_major avg `0.2678` n `8`; equity avg `0.1333` n `132`; fx avg `-0.0076` n `6`; index avg `0.0299` n `26`; metal avg `0.0374` n `20`; unknown avg `0.0904` n `792`
- 1h: commodity avg `-0.0887` n `12`; crypto_alt avg `0.031` n `232`; crypto_major avg `-0.1592` n `8`; equity avg `-0.2177` n `132`; fx avg `-0.017` n `6`; index avg `-0.0286` n `26`; metal avg `-0.1287` n `20`; unknown avg `2.2517` n `790`
- 4h: commodity avg `0.0761` n `12`; crypto_alt avg `0.1796` n `232`; crypto_major avg `0.0787` n `8`; equity avg `-0.0973` n `132`; fx avg `-0.0738` n `6`; index avg `-0.0032` n `26`; metal avg `-0.205` n `20`; unknown avg `0.2727` n `790`
- 24h: commodity avg `0.9474` n `12`; crypto_alt avg `-0.7985` n `232`; crypto_major avg `-1.7994` n `8`; equity avg `-2.3297` n `130`; fx avg `-0.0234` n `6`; index avg `-0.3988` n `26`; metal avg `-1.1424` n `20`; unknown avg `-0.0264` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0465`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0401`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0372`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0345`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0293`, n `668`, weak_sample_signal
