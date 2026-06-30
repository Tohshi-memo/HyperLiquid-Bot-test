# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T13:52:31.940953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1075` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0293` n `12`; crypto_alt avg `0.6958` n `228`; crypto_major avg `0.6887` n `8`; equity avg `0.18` n `88`; fx avg `-0.0029` n `6`; index avg `0.0513` n `23`; metal avg `0.0966` n `20`; unknown avg `0.5827` n `765`
- 1h: commodity avg `-0.0321` n `12`; crypto_alt avg `0.5826` n `228`; crypto_major avg `0.5285` n `8`; equity avg `0.4538` n `88`; fx avg `0.0067` n `6`; index avg `0.107` n `23`; metal avg `0.1261` n `20`; unknown avg `0.4803` n `765`
- 4h: commodity avg `0.0909` n `12`; crypto_alt avg `-0.9676` n `228`; crypto_major avg `-0.9591` n `8`; equity avg `0.0934` n `88`; fx avg `0.0015` n `6`; index avg `0.1484` n `23`; metal avg `-0.0697` n `20`; unknown avg `0.356` n `765`
- 24h: commodity avg `0.2911` n `12`; crypto_alt avg `-1.5429` n `228`; crypto_major avg `-0.6602` n `8`; equity avg `1.5566` n `88`; fx avg `0.0804` n `6`; index avg `0.2899` n `23`; metal avg `0.1828` n `20`; unknown avg `8.6783` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0472`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0467`, n `668`, weak_sample_signal
