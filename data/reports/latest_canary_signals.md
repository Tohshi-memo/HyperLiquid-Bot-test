# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T09:37:33.678717+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0477` n `13`; crypto_alt avg `0.0433` n `234`; crypto_major avg `0.0846` n `8`; equity avg `-0.0129` n `142`; fx avg `0.019` n `6`; index avg `0.0042` n `26`; metal avg `0.0188` n `20`; unknown avg `-0.09` n `975`
- 1h: commodity avg `-0.2414` n `13`; crypto_alt avg `0.37` n `234`; crypto_major avg `0.4915` n `8`; equity avg `0.3105` n `142`; fx avg `0.0182` n `6`; index avg `0.0843` n `26`; metal avg `0.0363` n `20`; unknown avg `0.4593` n `973`
- 4h: commodity avg `0.4625` n `13`; crypto_alt avg `-0.8752` n `234`; crypto_major avg `-0.6183` n `8`; equity avg `-0.5689` n `142`; fx avg `-0.0039` n `6`; index avg `-0.1651` n `26`; metal avg `-0.4178` n `20`; unknown avg `4.24` n `930`
- 24h: commodity avg `-0.0393` n `13`; crypto_alt avg `-0.4022` n `234`; crypto_major avg `0.223` n `8`; equity avg `0.3589` n `142`; fx avg `0.11` n `6`; index avg `0.1095` n `26`; metal avg `-0.3513` n `20`; unknown avg `776.8808` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1684`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
