# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T13:07:28.609588+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2281` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.4499` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1524` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0044` n `12`; crypto_alt avg `0.0939` n `233`; crypto_major avg `-0.0052` n `8`; equity avg `-0.0294` n `134`; fx avg `-0.0031` n `6`; index avg `-0.0012` n `26`; metal avg `0.0081` n `20`; unknown avg `-0.2362` n `795`
- 1h: commodity avg `0.1076` n `12`; crypto_alt avg `-0.8413` n `233`; crypto_major avg `-1.2869` n `8`; equity avg `-0.8806` n `134`; fx avg `-0.0103` n `6`; index avg `-0.1345` n `26`; metal avg `-0.2681` n `20`; unknown avg `0.0889` n `789`
- 4h: commodity avg `0.4989` n `12`; crypto_alt avg `-1.3016` n `233`; crypto_major avg `-1.7292` n `8`; equity avg `-1.5258` n `134`; fx avg `0.0108` n `6`; index avg `-0.2793` n `26`; metal avg `-0.8018` n `20`; unknown avg `-0.0496` n `789`
- 24h: commodity avg `0.4881` n `12`; crypto_alt avg `-5.7049` n `233`; crypto_major avg `-4.7169` n `8`; equity avg `-2.2908` n `134`; fx avg `0.0968` n `6`; index avg `-0.2835` n `26`; metal avg `-0.8788` n `20`; unknown avg `-1.1113` n `669`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
