# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T14:07:25.556365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0428` n `12`; crypto_alt avg `-0.1` n `232`; crypto_major avg `0.0105` n `8`; equity avg `0.2457` n `133`; fx avg `0.0091` n `6`; index avg `0.0715` n `26`; metal avg `0.0547` n `20`; unknown avg `0.138` n `789`
- 1h: commodity avg `0.0143` n `12`; crypto_alt avg `0.4661` n `232`; crypto_major avg `0.7691` n `8`; equity avg `0.4397` n `133`; fx avg `-0.0883` n `6`; index avg `0.0997` n `26`; metal avg `0.3475` n `20`; unknown avg `0.4467` n `789`
- 4h: commodity avg `-0.216` n `12`; crypto_alt avg `0.5658` n `232`; crypto_major avg `0.9953` n `8`; equity avg `1.0547` n `133`; fx avg `-0.166` n `6`; index avg `0.2201` n `26`; metal avg `0.7414` n `20`; unknown avg `0.7136` n `789`
- 24h: commodity avg `0.4722` n `12`; crypto_alt avg `-1.2136` n `232`; crypto_major avg `-1.6841` n `8`; equity avg `-0.233` n `132`; fx avg `-0.3606` n `6`; index avg `-0.0742` n `26`; metal avg `0.238` n `20`; unknown avg `0.0918` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
