# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T23:07:25.700441+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0139` n `13`; crypto_alt avg `0.0812` n `235`; crypto_major avg `0.0546` n `8`; equity avg `0.0222` n `143`; fx avg `0.0042` n `6`; index avg `-0.0055` n `26`; metal avg `-0.001` n `20`; unknown avg `-0.0471` n `982`
- 1h: commodity avg `0.0435` n `13`; crypto_alt avg `0.3271` n `235`; crypto_major avg `0.4031` n `8`; equity avg `0.0498` n `143`; fx avg `0.0027` n `6`; index avg `0.0635` n `26`; metal avg `0.005` n `20`; unknown avg `0.7801` n `982`
- 4h: commodity avg `0.3561` n `13`; crypto_alt avg `0.7692` n `235`; crypto_major avg `0.4474` n `8`; equity avg `0.1607` n `143`; fx avg `-0.0113` n `6`; index avg `0.0297` n `26`; metal avg `0.0494` n `20`; unknown avg `-0.2988` n `906`
- 24h: commodity avg `0.1379` n `13`; crypto_alt avg `-0.6622` n `235`; crypto_major avg `-0.3784` n `8`; equity avg `0.6787` n `142`; fx avg `-0.1422` n `6`; index avg `0.2715` n `26`; metal avg `-0.2195` n `20`; unknown avg `-0.6232` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
