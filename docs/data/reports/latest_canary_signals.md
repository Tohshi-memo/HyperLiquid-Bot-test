# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T15:22:28.124428+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.3455` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0333` n `12`; crypto_alt avg `0.0829` n `229`; crypto_major avg `0.1894` n `8`; equity avg `-0.0682` n `91`; fx avg `-0.0224` n `6`; index avg `-0.0178` n `25`; metal avg `-0.0826` n `20`; unknown avg `-0.0994` n `763`
- 1h: commodity avg `0.0897` n `12`; crypto_alt avg `0.5122` n `229`; crypto_major avg `0.889` n `8`; equity avg `0.0455` n `91`; fx avg `-0.0086` n `6`; index avg `-0.0383` n `25`; metal avg `-0.1087` n `20`; unknown avg `2.124` n `763`
- 4h: commodity avg `0.2089` n `12`; crypto_alt avg `-0.2172` n `229`; crypto_major avg `0.6017` n `8`; equity avg `-1.7438` n `91`; fx avg `-0.0172` n `6`; index avg `-0.1918` n `25`; metal avg `-0.0889` n `20`; unknown avg `2.2432` n `763`
- 24h: commodity avg `0.5443` n `12`; crypto_alt avg `0.3011` n `229`; crypto_major avg `0.915` n `8`; equity avg `-3.5979` n `90`; fx avg `-0.1895` n `6`; index avg `-0.6833` n `25`; metal avg `-0.105` n `20`; unknown avg `0.1522` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
